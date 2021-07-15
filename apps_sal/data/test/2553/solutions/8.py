t = int(input())
for _ in range(t):
    n, x = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    assert len(arr) == n
    num_odd = len([a for a in arr if a % 2 == 1])
    num_even = len([a for a in arr if a % 2 == 0])

    # o <= odd, e <= even, o+e = x, o is odd
    for i in range(num_odd+1):
        if i % 2 == 1 and 0 <= x - i <= num_even:
            print("Yes")
            break
    else:
        print("No")
    

