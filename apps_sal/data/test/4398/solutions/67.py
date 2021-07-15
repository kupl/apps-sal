n = int(input())
s,t = input().split()
st_mix = []

# sとtの1文字目からn文字目までをst_mixに加えていく
for i in range(0,n):
    st_mix.append(s[i]+t[i])
# リストの中身を結合
print("".join(st_mix))
