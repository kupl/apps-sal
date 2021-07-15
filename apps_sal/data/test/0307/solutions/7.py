a2,a3,a5,a6 = map(int,input().split())
s256 = min(a2,a5,a6)
a2 -= s256
a5 -= s256
a6 -= s256
s32 = min(a2,a3)
print(s256*256+s32*32)
