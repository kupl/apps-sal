N = int(input())
Blue = [input() for _ in range(N)]
M = int(input())
Red = [input() for _ in range(M)]
Word = Blue + Red
Word = list(set(Word))
ans = 0
for i in range(len(Word)):
    cnt = 0
    cnt += Blue.count(Word[i])
    cnt -= Red.count(Word[i])
    ans = max(ans,cnt)
print(ans)
