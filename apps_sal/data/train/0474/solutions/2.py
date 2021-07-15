from collections import defaultdict, Counter
import copy


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def score_of_word(w, score=score):
            ws = 0
            for c in w:
                ws += score[ord(c)-97]
                
            return ws
        
        letter_dict = defaultdict(int)
        for c in letters: letter_dict[c]+=1
            
        def remove_word_from_letter_dict(w, let_dict):
            for c in w:
                let_dict[c] -= 1
                if not let_dict[c]:
                    del let_dict[c]
                    
        def is_word_exist_in_letter_dict(w, let_dict):
            wc = Counter(w)
            for c, f in wc.items():
                if c not in let_dict or let_dict[c] < f:
                    return False
                
            return True
        
        def search_best_score(words, letter_dict, current_score=0):
            best_score = current_score
            for i in range(len(words)):
                w = words[i]
                if is_word_exist_in_letter_dict(w, letter_dict):                    
                    score = current_score + score_of_word(w)
                    copy_letter_dict = copy.deepcopy(letter_dict)
                    remove_word_from_letter_dict(w, copy_letter_dict)
                    score = search_best_score(words[i+1:], copy_letter_dict, score)
                    if score > best_score:
                        best_score = score
                        
            return best_score
        
        return search_best_score(words, letter_dict)
