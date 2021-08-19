# -*- coding: utf-8 -*-
import re
s = input()

if re.search(r's$', s):
    print(s + "es")
else:
    print(s + "s")
