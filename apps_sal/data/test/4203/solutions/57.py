s = input()
cnt = 0

def end():
  print("WA")
  return

if len(s) < 3:
    end()

if s[0] == "A" and s.count("C") == 1:
    if "C" in s[2:-1]:
        for i in s:
            if i == i.upper():
                cnt += 1
        if cnt == 2:
            print("AC")
            return

end()
