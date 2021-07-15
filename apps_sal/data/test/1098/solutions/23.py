n = int(input())
minutes = []
for i in range(n):
    s = input()
    minutes.append(int(s[:-3]) * 60 + int(s[-2:]))
minutes.sort()

max = 0
for i in range(0, n - 1):
    cur = minutes[i + 1] - minutes[i] - 1;
    
    if cur > max:
        max = cur

cur = 24*60 - (minutes[-1] - minutes[0]) - 1
if cur > max:
    max = cur

hours = max // 60
minutes = max - hours * 60

h_str = str(hours)
if len(h_str) < 2:
    h_str = "0" + h_str
    
m_str = str(minutes)
if len(m_str) < 2:
    m_str = "0" + m_str
    
print(h_str+":"+m_str)
