import collections
def i_input(): return int(input())
def i_map(): return list(map(int, input().split()))
def i_list(): return list(map(int, input().split()))
def i_row(N): return [int(input()) for _ in range(N)]
def i_row_list(N): return [list(input().split()) for _ in range(N)]

n=i_input()
ss=[input() for _ in range(n)]
ss.sort()

css=collections.Counter()
for s in ss:
    css[s]+=1
maxapper=max(css.values())

for w in css:
    if css[w]==maxapper:
        print(w)




