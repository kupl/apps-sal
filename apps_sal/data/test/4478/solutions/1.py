import sys

class Scanner():
    def __init__(self):
        self.tokens = []
        self.index = -1
	
        for line in sys.stdin:
            self.tokens.extend(line.split())
    
    def next_token(self):
        self.index += 1
        return None if self.index == len(self.tokens) \
		            else self.tokens[self.index]

def main():
    scanner = Scanner()
    n = int(scanner.next_token())
    
    sequences = []
    for i in range(n):
        k = int(scanner.next_token())
        sequences.append([int(scanner.next_token()) for _ in range(k)])
    
    mp = dict()
    for i, ar in enumerate(sequences):
        s = sum(ar)
        for j, v in enumerate(ar):
            x = s - v
            if x in mp:
                print("YES")
                print("{} {}".format(mp[x][0] + 1, mp[x][1] + 1))
                print("{} {}".format(i + 1, j + 1))
                return
        
        for j, v in enumerate(ar):
            mp[s - v] = (i, j)
    
    print("NO")
    
def __starting_point():
    main()

__starting_point()
