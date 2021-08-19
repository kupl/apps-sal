n = int(input())
n1 = input().split()

n2 = []
s1 = set()
for x in n1:
    n2.append(int(x))
    s1.add(int(x))

n2.sort()

maxy = n2[len(n2) - 1] - n2[0]

count = 0
num = 1

while(num < maxy):
    num = num * 2
    count = count + 1

flag = 0
base0 = 0
base1 = 0
base2 = -1

cflag = 0

for x in n2:
    for z in range(0, count + 1):
        # print(z)
        if(x + 2**z in s1):
            if(flag == 0):
                flag = 1
                base0 = x
                base1 = x + 2**z
            if(x + 2**(z + 1) in s1):
                cflag = 1
                base0 = x
                base1 = x + 2**z
                base2 = x + 2**(z + 1)
                break
    if(cflag == 1):
        break

if(cflag == 1):
    s = "3\n" + str(base0) + " " + str(base1) + " " + str(base2)
    print(s)
if(cflag == 0 and flag == 1):
    s = "2\n" + str(base0) + " " + str(base1)
    print(s)
if(cflag == 0 and flag == 0):
    s = "1\n" + str(n2[0])
    print(s)
