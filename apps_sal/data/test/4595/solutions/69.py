s = input()

first_A_find = s.find("A")
end_Z_find = s.rfind("Z") + 1

print(end_Z_find - first_A_find)
