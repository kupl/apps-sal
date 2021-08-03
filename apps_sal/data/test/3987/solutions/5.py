n = int(input())

a, ab, aba, abab = 0, 0, 0, 0

b = [int(x) for x in input().split()]

for x in b:

    if x == 1:

        a += 1

        aba += 1

    else:

        ab += 1

        abab += 1

    ab = max(a, ab)

    aba = max(aba, ab)

    abab = max(abab, aba)

print(abab)


# Made By Mostafa_Khaled
