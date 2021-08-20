n = int(input())
s = [input() for _ in range(2)]
mod = 10 ** 9 + 7
' \nたて*たて = *2\nたて*よこ = *2\nよこ*よこ = *3 (1,2)=(2,3)(2,1),(3,1)\nよこ*たて = *1\n'
tmp = 1
pos = 0
pre_state = -1
while pos < n:
    if s[0][pos] == s[1][pos]:
        if pos == 0:
            tmp *= 3
        elif pre_state == 0:
            tmp *= 2
        else:
            tmp *= 1
        pre_state = 0
        pos += 1
    else:
        if pos == 0:
            tmp *= 6
        elif pre_state == 0:
            tmp *= 2
        else:
            tmp *= 3
        pre_state = 1
        pos += 2
    tmp %= mod
print(tmp)
