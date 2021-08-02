string = input()
k = int(input())

if k > len(string):
    print('impossible')
else:
    different = set(string)
    if len(different) >= k:
        print(0)
    else:
        print(k - len(different))
