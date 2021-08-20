n = int(input())
cn1 = n
cn2 = n * (n - 1) // 2
cn3 = cn2 * (n - 2) // 3
cn4 = cn3 * (n - 3) // 4
cn5 = cn4 * (n - 4) // 5
a = cn1 + 4 * cn2 + 6 * cn3 + 4 * cn4 + cn5
b = cn1 + 2 * cn2 + cn3
print(a * b)
