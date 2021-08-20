N = int(input())
fb_list = []
for i in range(1, N + 1):
    if i % 5 != 0 and i % 3 != 0:
        fb_list.append(i)
ans = sum(fb_list)
print(ans)
