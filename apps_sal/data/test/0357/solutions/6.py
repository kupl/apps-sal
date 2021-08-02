s = input()
c = 0
c += s.count("Danil")
c += s.count("Olya")
c += s.count("Slava")
c += s.count("Ann")
c += s.count("Nikita")

if c == 1:
    print("YES")
else:
    print("NO")
