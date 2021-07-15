s = input()
start = s.find('A')
end = s.rfind('Z',start)
print(end - start + 1)
