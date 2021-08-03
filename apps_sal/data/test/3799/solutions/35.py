def remove(s):
    i = 1
    count = 0
    while i < len(s) - 1:
        if s[i - 1] != s[i + 1]:
            s.pop(i)
            count += 1
        i += 1
    return count


s = list(input())
count = 0
while True:
    tmp = remove(s)
    if tmp == 0:
        break
    count += tmp

if count % 2 == 0:
    print("Second")
else:
    print("First")
