n = int(input())
s = input()
if n == 1:
    print("Yes")
    return
else:
    val = [0 for i in range(26)]
    for i in s:
        val[ord(i) - ord('a')] += 1
    k = max(val)
    if k >= 2:
        print("Yes")
    else:
        print("No")
