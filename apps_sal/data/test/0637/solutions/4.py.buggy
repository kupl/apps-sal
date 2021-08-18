input()

picture = input().split()

cur_col = picture[0]
cur_len = 0
last_len = -1


for i in picture:
    if i == cur_col:
        cur_len += 1
    else:
        if last_len != -1 and cur_len != last_len:
            print("NO")
            return
        else:
            last_len = cur_len
            cur_len = 1
            cur_col = i

if last_len != -1 and cur_len != last_len:
    print("NO")
    return

print("YES")
