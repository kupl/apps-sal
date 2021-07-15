from collections import Counter
def main():
    N = int(input())
    V = [int(a) for a in input().split()]
    
    even = list()
    odd = list()

    for i in range(N):
        if (i + 1) % 2 == 0:
            odd.append(V[i])
        else:
            even.append(V[i])

    even_counter = Counter(even).most_common()
    odd_counter = Counter(odd).most_common()

    ans = 0
    if even_counter[0][0] != odd_counter[0][0]:
        if len(even_counter) >= 2:
            ans += len(even) - even_counter[0][1]

        if len(odd_counter) >= 2:
            ans += len(odd) - odd_counter[0][1]

    else:
        if len(even_counter) == 1 and len(odd_counter) == 1:
            ans += even_counter[0][1]

        elif len(even_counter) == 1 and len(odd_counter) >= 2:
            ans += len(odd) - odd_counter[1][1]

        elif len(even_counter) >= 2  and len(odd_counter) == 1:
            ans += len(even) - even_counter[1][1]

        elif len(even_counter) >= 2 and len(odd_counter) >= 2:
            cost_even = len(even) - even_counter[0][1] + len(odd)  - odd_counter[1][1]
            cost_odd  = len(odd)  - odd_counter[0][1]  + len(even) - even_counter[1][1]

            ans += min(cost_even, cost_odd)

    print(ans)

def __starting_point():
    main()
__starting_point()
