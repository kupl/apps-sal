from collections import defaultdict, deque

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) <= 1:
            return len(words)
        
        graph_dict, len_words_dict = self.getGraphDict(words)
 
        word_lengths = list(len_words_dict.keys())
        word_lengths.sort()
        
        return self.bfsWordChain(graph_dict, len_words_dict, word_lengths)
    
    def bfsWordChain(self, graph_dict, len_words_dict, word_lengths):
        word_lenghts_index = 0
        initial_words = len_words_dict[word_lengths[0]]
        
        max_possible_length = len(word_lengths)
        curr_length = 1

        visited = set()
        
        queue = deque()
        for word in initial_words:
            queue.append((word, 1))
            visited.add(word)
        
        max_len_so_far = 1
        
        while queue:
            this_item = queue.popleft()
            this_word = this_item[0]
            this_chain_len = this_item[1]
            max_len_so_far = max(max_len_so_far, this_chain_len)
            # this_item_possible_length = this_chain_len + len(word_lengths[])
            neighbors = graph_dict[this_word]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, this_chain_len + 1))
            
            if len(queue) == 0:
                word_found = False
                for word_length in word_lengths:
                    for word in len_words_dict[word_length]:
                        if word not in visited and not word_found:
                            queue.append((word, 1))
                            visited.add(word)
                            word_found = True
                            break
        
        return max_len_so_far
            
        
        

    
    def getGraphDict(self, words):
        len_words_dict = defaultdict(list)
        for word in words:
            len_words_dict[len(word)].append(word)
        word_lenghts_arr = []
        graph_dict = defaultdict(list)
        for word_length in len_words_dict:
            for predecessor in len_words_dict[word_length]:
                if word_length + 1 in len_words_dict:
                    for word in len_words_dict[word_length + 1]:
                        if self.isPredecessor(predecessor, word):
                            graph_dict[predecessor].append(word)

        return graph_dict, len_words_dict
    
    def isPredecessor(self, predecessor, word):
        predecessor_index = 0
        word_index = 0
        while predecessor_index < len(predecessor) and word_index < len(word):
            if predecessor[predecessor_index] == word[word_index]:
                predecessor_index += 1
                word_index += 1
            else:
                word_index += 1
        
        if word_index == predecessor_index + 1 or word_index == predecessor_index:
            return True
        else:
            return False

