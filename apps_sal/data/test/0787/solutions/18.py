from collections import OrderedDict
count = int(input())
line = input()

uniq = "".join(OrderedDict.fromkeys(line).keys())

if count > len(uniq):
    print("NO")
else:
    print("YES")
    if count == len(uniq):
        while len(line) != 0:
            first_uniq = 0
            uniq = uniq[1:]
            if len(uniq) == 0:
                print(line)
                break
            last_uniq = line.find(uniq[0])
            print(line[first_uniq:last_uniq])
            line = line[last_uniq:]
    else:
        while count != 1:
            first_uniq = 0
            uniq = uniq[1:]
            last_uniq = line.find(uniq[0])
            print(line[first_uniq:last_uniq])
            line = line[last_uniq:]
            count -= 1
        print(line)
