import sys
sys.setrecursionlimit(10**7)

n = int(input())
cnt = []

def search(x, use):
    if x > n:
        return
    if use == 0b111:
        cnt.append(1)
        
    search(x * 10 + 3, use | 0b100)
    search(x * 10 + 5, use | 0b010)
    search(x * 10 + 7, use | 0b001)

search(0, 0)
print(sum(cnt))
