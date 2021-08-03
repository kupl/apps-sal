a, ta = map(int, input().split())
b, tb = map(int, input().split())
s = input()
ha = int(s[0]) * 10 + int(s[1])
ma = int(s[3]) * 10 + int(s[4])

startH = ha * 60 + ma
endH = startH + ta
st = 300
k = 0
while st < endH and st < 1440:
    if st + tb > startH:
        k += 1
    st = st + b
print(k)
