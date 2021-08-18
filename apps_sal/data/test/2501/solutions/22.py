from collections import defaultdict

N = int(input())
*A, = map(int, input().split())

'''
方針:
- 各A_i,(i<h)ごとにf(h,j)=A_h+A_j-|h-j|の値がf(i,j)に比べてどれだけ変化するかを計算し、
リストに格納(①)
- 各要素A_k,(j<k)ごとにf(i,k)=A_i+A_k-|i-k|の値がf(i,j)に比べてどれだけ変化するかを
計算し、カウントをとる(②)
- 再度ループを回して①と②を照合し、値が一致する組数をansに加算
'''

ans = 0
diff_list = []
count = defaultdict(int)
for i in range(1, N):
    if i == A[0] + A[i]:
        ans += 1
    d1 = A[i] - A[0]
    d2 = i
    diff_list.append(d1 + d2)

    count[A[0] + A[i] - i] += 1

for i in range(N - 1):
    count[A[0] + A[i + 1] - (i + 1)] -= 1
    d = diff_list[i]
    ans += count[-d]

print(ans)
