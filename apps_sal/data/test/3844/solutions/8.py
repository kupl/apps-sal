from collections import Counter

_ = input()
count = Counter([int(x) for x in input().split()])

for key in sorted(count.keys())[::-1]:
    if count[key] % 2 == 1:
        print('Conan')
        break
else:
    print('Agasa')

