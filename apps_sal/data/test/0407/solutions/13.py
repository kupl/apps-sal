ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
a = [0] * 10  # array to store total decimal value of each element index wise
initial = []  # stores initials of each string
n = int(input())
for i in range(n):
    s = input()
    initial.append(s[0])
    for j in range(len(s)):
        a[ch.index(s[j])] += 10**(len(s) - j - 1)
sum = 0  # final sum
flag = False  # turns true after we have assigned zero
count = 1  # digits we assign to each character
for k in range(10):
    maxFreq = 0  # stores max value of an char from a array
    for l in range(10):  # finds max value from a and assigns it to maxFreq var
        if maxFreq < a[l]:
            maxFreq = a[l]

    temp = a.index(maxFreq)
    currChar = ch[temp]
    a[temp] = 0
    if currChar not in initial and not flag:
        flag = True  # we have assigned this currChar 0 and now we switch flag
    else:
        sum += maxFreq * count
        count += 1  # 1 has been assigned now we assign 2 and so on...
print(sum)
