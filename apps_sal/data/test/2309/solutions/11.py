from collections import deque

if True:
    N = int(input())
    # X = [[[] for _ in range(5)] for i in range(500001)]
    X = {}
    def calc(t):
        c = 0
        v = 0
        for u in reversed(t):
            if u == "a" or u == "i" or u == "u" or u == "e" or u == "o":
                if c == 0:
                    if u == "a": v = 0
                    if u == "i": v = 1
                    if u == "u": v = 2
                    if u == "e": v = 3
                    if u == "o": v = 4
                c += 1
        if c not in X:
            X[c] = [[] for _ in range(5)]
        
        X[c][v].append(t)

    for _ in range(N):
        calc(input())
else:
    N = 14
    X = [[[], [], [], [], []], [['am', 'that'], ['this', 'is', 'first', 'mcdics', 'i'], [], ['the'], ['wow']], [[], [], ['round', 'proud'], [], []], [['hooray'], [], ['about'], [], []], [[], [], [], ['codeforces'], []]]
# print("X =", X)
A = 0
B = 0
Q = deque([])
for i in X:
    # print("X[i] =", X[i])
    # print([len(x)//2 for x in X[i]])
    a = sum([len(x)//2 for x in X[i]]) * 2
    b = sum([len(x) for x in X[i]])//2*2 - a
    A += a
    B += b
    # print("a, b, A, B =", a, b, A, B)
    for j in range(5):
        while len(X[i][j]) >= 2:
            deque.appendleft(Q, X[i][j].pop())
            deque.appendleft(Q, X[i][j].pop())
    
    for j in range(5):
        while len(X[i][j]) >= 1 and b > 0:
            deque.append(Q, X[i][j].pop())
            b -= 1
    # print("Q =", Q)

ans = min(A//2, (A+B)//4)
print(ans)
for _ in range(ans):
    print(Q.pop(), Q.popleft())
    print(Q.pop(), Q.popleft())


