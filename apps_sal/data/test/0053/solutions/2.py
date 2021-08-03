# https://pymotw.com/2/collections/counter.html
# same code as mmaxio
from collections import Counter


def r(): return list(map(int, input().split()))


def main():
    n, = r()
    s = input()
    cost = list(r())

    ans = 0

    cnt = Counter()

    for i in range(n // 2):
        if s[i] == s[n - 1 - i]:
            ans += min(cost[i], cost[n - 1 - i])
            cnt[s[i]] += 1
    total = sum(cnt.values())
    if total > 0:
        ch, occ = cnt.most_common(1)[0]
        avail = []
        if occ > total - occ:  # if highest occurence is more than the 50% of total then we will look for the letters which does not have pairs and are not equal to the letter with the highest ocuurence
            for i in range(n // 2):
                if s[i] != s[n - 1 - i] and s[i] != ch and s[n - 1 - i] != ch:
                    avail.append(min(cost[i], cost[n - 1 - i]))
            avail.sort()
            ans += sum(avail[:2 * occ - total])

    print(sum(cost) - ans)


main()
# suppose total is 100 and highest occ is 51...difference between highest occ and remaining can be found using this form 2*occ-total as it is a simplified form of two steps 1.total-occ=remaining and 2.occ-remaining which is this case is 2 if highest occ is <= 50 % of total then it can be satisfied by remaining 50% but if it is greater than 50% then we have to use the letters of of the total
