A, B = map(int, input().split())
# ans = 0
# for i in range(40):
#     # 含まれる1の数を数える
#     tmp = (B-A) // 2**(i+1) * 2**i
#     p = A%(2**(i+1))
#     q = (B-A)%(2**(i+1))
#     # p から p+qの中で余りが2**i ~ 2**(i+1)-1になる個数を求める
#     tmp += max(min(p+q,2**(i+1)-1) - max(p,2**i)+1,0)
#     tmp += max(min(p+q,2**(i+1)-1 + 2**(i+1)) - max(p,2**i + 2**(i+1))+1,0)
#     ans += (tmp%2) * 2**i
# print(ans)

def f(N):
    if N % 2 == 1:
        return ((N+1)//2)%2
    else:
        return ((N//2)%2)^N

print(f(A-1)^f(B))
