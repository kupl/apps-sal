def fun(string):
    last = ''
    amount = 0
    saw = False
    r = len(string)
    for i in range(r - 1, -1, -1):
        if string[i] in gay:
            amount += 1
            if not saw:
                saw = True
                last = string[i]
    return amount, last


def main():
    n = int(input())
    # to hack this solution write any test with n == 2e5, TLE
    words = {}
    sizesandlasts = {}
    sizes = set()
    for i in range(n):
        s = input()
        pair = size, last = fun(s)
        sizes.add(size)
        words[s] = pair
        if pair not in sizesandlasts:
            sizesandlasts[pair] = []
        sizesandlasts[pair].append(s)

    second = []
    first = {}
    for length in sizes:
        for ch in gay:
            text = sizesandlasts.get((length, ch), [])
            for val in range(len(text) // 2):
                second.append([text.pop(), text.pop()])
            if len(text) > 0:
                size = words[text[0]][0]
                if size not in first:
                    first[size] = []
                first[size].append(text.pop())

    ans = []
    for size in first:
        if len(second) == 0:
            break
        else:
            while len(first[size]) > 1 and len(second) > 0:
                ans.append([[first[size].pop(), first[size].pop()], second.pop()])
    while len(second) > 1:
        ans.append([second.pop(), second.pop()])
    print(len(ans))
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0][0], ans[i][1][0]))
        print("{} {}".format(ans[i][0][1], ans[i][1][1]))


gay = set()
for char in ['a', 'e', 'o', 'i', 'u']:
    gay.add(char)
main()
