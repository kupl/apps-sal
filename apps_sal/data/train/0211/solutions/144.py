def get_sequences(symbols, length):
    if length == 0:
        return [[]]
    
    sequences = []
   
    tail_sequences = get_sequences(symbols, length-1)
    
    for tail_sequence in tail_sequences:
        for symbol in symbols:
            sequences.append(list(tail_sequence)+[symbol])
    
    return sequences
            

def is_unique(sequence, s):
    if s=='':
        return 0
    
    words = set()
    letters = [s[0]]
    for i in range(len(sequence)):
        if sequence[i] == 1:
            word = ''.join(letters)
            if word in words:
                return False
            words.add(word)
            letters = [s[i+1]]
        else:
            letters.append(s[i+1])
    
    word = ''.join(letters)
    if word in words:
        return False
    
    return True
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        sequences = get_sequences([0,1], len(s)-1)
        
        max_split = 1
        for sequence in sequences:
            if is_unique(sequence, s):
                max_split = max(max_split, sum(sequence)+1)
                
        return max_split
                

