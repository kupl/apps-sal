d = 3 * 10**10
n = int(input())
s = input()
a = 0
b = 0
i = 0
j = n - 1
while i < n and s[i] == '1':
    i += 1
    a += 1
while j >= 0 and s[j] == '1':
    b += 1
    j -= 1
if n == 1 and s[0] == '1':
    print(((d // 3) * 2))
elif a <= 2 and b <= 2:
    if not (j - i) % 3:
        x = '011' * ((j - i) // 3)
        if x == s[i:j]:

            maxindex = d + 1 - n
            if n == 1:
                if s[0] == '1':
                    print(((d // 3) * 2))
                else:
                    print((d // 3))
            elif a == 0:
                print((maxindex // 3))
            elif a == 1:
                print(((maxindex + 1) // 3))
            else:
                print(((maxindex + 2) // 3))
        else:
            print((0))

    else:
        print((0))
else:
    print((0))
