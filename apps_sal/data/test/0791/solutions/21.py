n = int(input())
box = input()
ans = 1
if box[0] == '0':
    pass
else:
    for bit in box:
        if bit == '1':
            ans += 1
        else:
            break
print(min(ans, n))
