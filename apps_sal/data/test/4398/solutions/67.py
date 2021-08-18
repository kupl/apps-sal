n = int(input())
s, t = input().split()
st_mix = []

for i in range(0, n):
    st_mix.append(s[i] + t[i])
print("".join(st_mix))
