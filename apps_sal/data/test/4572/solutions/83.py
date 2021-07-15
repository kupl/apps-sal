s = input()
d_l = [chr(i) for i in range(97, 97+26)]
ans = None
for d in d_l:
    if d not in list(s):
        ans = d
        break
print(ans)
