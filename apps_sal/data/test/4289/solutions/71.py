N = int(input())
(T, A) = map(int, input().split())
H = map(int, input().split())
candidates = list(H)
decide = []
for candidate in candidates:
    temparature = T - candidate * 0.006
    decide.append(abs(A - temparature))
hope_place = min(decide)
print(decide.index(hope_place) + 1)
