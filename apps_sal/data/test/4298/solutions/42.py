N, D = map(int,input().split())

# 監視員は2D+1本の木を見れる
kanshi = 2 * D + 1

print(N//kanshi if N%kanshi==0 else N//kanshi+1)
