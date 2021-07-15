N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
eat = lambda x: (D-1)//x+1
ans = sum(eat(a) for a in A) + X
print(ans)
