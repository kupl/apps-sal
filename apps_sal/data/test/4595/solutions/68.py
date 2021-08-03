s = input()

a_index = s.find('A')
z_index = s.rfind('Z')

print(z_index - a_index + 1)
