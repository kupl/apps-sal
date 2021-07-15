class Solution:
     def validIPAddress(self, IP):
         """
         :type IP: str
         :rtype: str
         """
         def is_hex(hexs):
             hex_set = set('0123456789abcdefABCDEF')
             return set(hexs)<hex_set
         
         result = 'Neither'
         if '.' in IP:
             sub_str = IP.split('.')
             if len(sub_str)!=4:
                 return result
             result = 'IPv4'
         elif ':' in IP:
             sub_str = IP.split(':')
             if len(sub_str) != 8:
                 return result
             result = 'IPv6'
         else:
             return result
         for sub in sub_str:
             if result == 'IPv4':
                 if not sub.isdigit():
                     result = 'Neither'
                     break                
                 if len(str(int(sub)))!=len(sub) or int(sub)>255:
                     result = 'Neither'
                     break
             if result == 'IPv6':
                 if len(sub)>4 or len(sub)==0 or not is_hex(sub):
                     result = 'Neither'
                     break
                     
         return result

