N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
def eat(x): return (D - 1) // x + 1


ans = sum(eat(a) for a in A) + X
print(ans)
