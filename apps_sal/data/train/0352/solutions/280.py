from collections import defaultdict, deque

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        lookup_neighbors = defaultdict(list)
        for word in words:
            word_length: int = len(word)
            lookup_neighbors[word_length].append(word)
        
        def is_next_word_valid(current_word: str, next_word: str) -> bool:
            current_word_length = len(current_word)
            
            for index in range(current_word_length):
                if next_word == current_word[0:index] + current_word[index + 1:]:
                    return True
                
            return False
        
        maximum_chain = 0
        
        for word in reversed(words):
            frontier = deque([(word, 1)])
            
            while frontier:
                next_frontier = deque()
                while frontier:
                    current_word, distance = frontier.popleft()
                    current_word_length = len(current_word)
                    maximum_chain = max(maximum_chain, distance)
                    
                    for neighbor in lookup_neighbors[current_word_length - 1]:
                        if is_next_word_valid(current_word, neighbor):
                            next_frontier.append((neighbor, distance + 1))
                
                frontier = next_frontier
            
        
        return maximum_chain
