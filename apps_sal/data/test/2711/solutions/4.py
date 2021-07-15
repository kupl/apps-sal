import os
import io
from collections import deque, defaultdict

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def li():return [int(i) for i in input().rstrip().split()]
def st():return str(input().rstrip())[2:-1]
def val():return int(input().rstrip())

# def li():return [int(i) for i in input().rstrip().split()]
# def st():return str(input())
# def val():return int(input())

#Input Reading

n,k = li()

pages = []
abc = set()

for _ in range(n):
    p = val()
    page = []
    for i in range(k):
        word = st()
        page.append(word)
    abc |= set(page[-1])
    pages.append((p,page))

pages.sort(key = lambda x: x[0])
words = []
for _,page in pages:
    words.extend(page)

if n == k == 1:
    print(''.join(abc))
    return

def match(w1,w2):
    for i in range(min(len(w1), len(w2))):
        if w1[i] == w2[i]:
            continue
        else:
            return (w1[i],w2[i])

    if len(w1) > len(w2):
        print("IMPOSSIBLE")
        return    

#Reading the graph and its indegrees
g = defaultdict(set)
indeg = defaultdict(int)

for i in range(len(words) - 1):
    out = match(words[i], words[i+1])
    if out is not None:
        c1,c2 = out
        if c2 not in g[c1]:
            g[c1].add(c2)
            indeg[c2] += 1


#Topsort things
ts = []
zero = deque()
for u in g:
    if indeg[u] == 0:
        zero.append(u)

while len(ts) != len(abc):
    if len(zero) == 0:
        print("IMPOSSIBLE")
        return
    
    u = zero.popleft()
    ts.append(u)
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            zero.append(v)

print("".join(ts))


