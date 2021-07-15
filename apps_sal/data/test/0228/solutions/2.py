n = int(input())
a = [int(i) for i in input().split()]
print("Alice" if sum([1 if i==min(a) else 0 for i in a ]) <= n/2 else "Bob")
