a = input().strip()
b = input().strip()
ans = 0

ai = len(a) - 1
bi = len(b) - 1

while ai >= 0 and bi >= 0:
    # print('ai',ai)
    #print('bi', bi)
    if a[ai] == b[bi]:
        #print(a[ai], 'and', b[bi], 'are the same')
        ans += 2
    else:
        #print(a[ai], 'and', b[bi], 'are not the same')
        break
    ai -= 1
    bi -= 1
# print(ans)
print(len(a) + len(b) - ans)
