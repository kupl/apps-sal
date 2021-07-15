n, k = list(map(int, input().strip().split()))
groups = list(map(int, input().strip().split()))


def fetch(delim, num_places):
    for i, g in enumerate(groups):
        num_g = min(g//delim, num_places)
        g -= num_g*delim
        num_places -= num_g
        groups[i] = g

        if num_places == 0:
            break

    return num_places

num_4 = fetch(4, n)
num_2 = fetch(2, 2*n) + num_4
num_2 += fetch(2, num_4)
if sum(groups) <= num_2:
    print("YES")
else:
    print("NO")

