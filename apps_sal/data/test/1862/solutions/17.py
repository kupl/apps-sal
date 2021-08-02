no_of_socks = int(input())
socks = []
for i in range(no_of_socks + 1):
    socks.append(0)
present = 0
maximum = 0
string = input()
i = 0
while i < len(string):
    j = 0
    if string[i] == " ":
        i += 1
    while string[i] != " ":
        j *= 10
        j += int(string[i])
        i += 1
        if i == len(string):
            break
    socks[j] += 1
    present += 1
    if(socks[j] == 2):
        present -= 2
    if(maximum < present):
        maximum = present

print(maximum)
