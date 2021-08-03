s = input()
n = len(s)

kol = 0
posl_i = 0
tek_i = s.find("bear", 0, n)
while(tek_i != -1):
    kol += (tek_i - posl_i + 1) * (n - tek_i - 3)
    posl_i = tek_i + 1
    tek_i = s.find("bear", tek_i + 1, n)

print(kol)
