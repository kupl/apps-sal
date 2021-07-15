s = input()
nums = []

f = "0"+str(len(s)-1)+"b"

for i in range(2**(len(s)-1)):
    m = format(i, f)

    l = 0
    r = 0
    while r < len(m):
        if m[r] == "1":
            nums.append(s[l:r+1])
            l = r+1
        r += 1

    nums.append(s[l:r+1])

print(sum(map(int, nums)))
