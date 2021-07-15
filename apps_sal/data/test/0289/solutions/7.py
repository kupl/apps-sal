s = input()
maxx = 0
for i in range(len(s)):
    news = s[:i] + 'V' + s[i+1:]
    maxx = max(news.count('VK'), maxx)
    news = s[:i] + 'K' + s[i + 1:]
    maxx = max(news.count('VK'), maxx)
print(maxx)

